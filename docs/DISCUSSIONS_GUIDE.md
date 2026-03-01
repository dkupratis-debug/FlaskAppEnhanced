# Discussions Guide

Use GitHub Discussions for learner questions, ideas, and progress updates.

## Audience

- Learners asking questions
- Maintainers moderating community threads

## Expected Outcome

After this guide, you should be able to:

1. Post in the correct discussion category
2. Moderate discussions with clear response standards
3. Convert actionable discussions into tracked issues/PRs

## Start Here

- Start Here discussion: `https://github.com/dkupratis-debug/FlaskAppEnhanced/discussions/29`
- Beginner click guide: `docs/FIRST_10_MINUTES.md`
- Main walkthrough: `docs/GITHUB_GUIDE.md`
- Engagement playbook: `docs/ENGAGEMENT_PLAYBOOK.md`
- Engagement automation: `docs/ENGAGEMENT_AUTOMATION.md`
- Weekly prompt template: `docs/templates/WEEKLY_DISCUSSION_PROMPT.md`
- Weekly check-in template: `docs/templates/WEEKLY_CHECKIN_TEMPLATE.md`
- Monthly recap template: `docs/templates/MONTHLY_RECAP_TEMPLATE.md`
- Learner support reply template: `docs/templates/LEARNER_HELP_RESPONSE_TEMPLATE.md`
- Maintainer cadence guide: `docs/ENGAGEMENT_PLAYBOOK.md`

## Which Category to Use

- `Q&A`: beginner questions, setup problems, workflow confusion
- `Ideas`: improvements to docs, training tasks, repo structure
- `Show and tell`: share learner progress, screenshots, or completed exercises
- `Announcements`: maintainer updates and major training changes
- `General`: anything that does not fit the categories above

## Maintainer Moderation Flow

1. Check new posts daily.
1. Answer `Q&A` posts with direct steps and file links.
1. Convert actionable ideas into Issues.
1. Close the loop by linking resolved PRs back into the discussion thread.
1. Remove secrets, tokens, or sensitive information immediately if posted.

## Weekly Check-In Signal

Use a consistent progress signal each week:

1. Open the latest weekly check-in issue (auto-created by workflow).
2. Ask learners to post progress or blockers.
3. Link blocked learners to exact docs path and one next step.
4. Roll unresolved blockers into monthly recap for process improvements.

## Response Time Expectations

- `Q&A`: initial maintainer response target is within 24 hours.
- `Learner help` style questions: target is same day when possible.
- `Ideas` and `Show and tell`: acknowledge within 48 hours.
- If an answer requires deeper investigation, post a status update in the thread so learners know it is being worked.

## Safety Rules for Public Learning

- Never post `.env` values, API keys, or access tokens.
- Keep all contributions through Pull Requests with CI checks.
- Keep branch protection enabled on `main`.
- Use `SECURITY.md` for vulnerability reports instead of public discussion threads.
