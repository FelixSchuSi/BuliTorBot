use crate::reddit_scrape::scrape_reddit_submission::RedditSubmission;

use super::{competition::Competition, videohost::VideoHost};
use chrono::Utc;
use log::info;

use std::str::FromStr;

const UNDER_7_TO_UNDER_21: [&str; 15] = [
    "u7", "u8", "u9", "u10", "u11", "u12", "u13", "u14", "u15", "u16", "u17", "u18", "u19", "u20",
    "u21",
];

/// Returns true if the submission counts as a goal video for the specified competition
pub fn submission_filter(submission: &RedditSubmission, competition: &Competition) -> bool {
    let lower_title = submission.title.to_lowercase();
    let mut title_split = lower_title.split_whitespace();

    info!(
        "Checking submission for competition {:?}: {}",
        competition.name, submission.title
    );

    // Check if the title contains two teams of the specified competition
    if !competition.is_valid_post_title_for_competition(&submission.title) {
        info!(
            "Title does not contain two teams of {:?}: {}",
            competition.name, submission.title
        );
        return false;
    }

    // Titles of goal videos are expected to be in the format: "team1 [1] - [0] team2"
    // So a valid title has to contain a hyphen
    if !title_split.any(|s| s.contains("-")) {
        info!("Title does not contain a hyphen: {}", submission.title);
        return false;
    }

    // Ignore all u7 to u21 games
    if title_split.any(|s| UNDER_7_TO_UNDER_21.contains(&s)) {
        info!(
            "Title contains an age group (u7 to u21): {}",
            submission.title
        );
        return false;
    }

    // Also ignore womens games
    if title_split.any(|s| s.to_lowercase() == "w") {
        info!("Title contains a womens game: {}", submission.title);
        return false;
    }

    // Check if the video is hosted on one of the specified VideoHosts
    if VideoHost::from_str(&submission.url).is_err() {
        info!("Video is not hosted on a valid host: {}", &submission.url);
        return false;
    }

    // // Submission must be younger than 10 minutes
    // if Utc::now().timestamp() - submission.created_utc as i64 > 600 {
    //     info!(
    //         "Submission is not younger than 10 minutes: {} {}",
    //         submission.title, submission.id
    //     );
    //     return false;
    // }

    info!(
        "✅ Submission passed filter for competition {:?}: {:?} {}",
        competition.name, submission.title, submission.id
    );

    return true;
}
