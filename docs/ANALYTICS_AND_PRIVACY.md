# Analytics and Privacy (Learning Repo + Demo App)

This guide explains how to track usage safely and ethically without compromising your repository or your users.

## What You Can Track on GitHub (No Code Changes Needed)

GitHub provides repository-level insights (if enabled/available), including:
- Views
- Unique visitors
- Clones
- Referrers (where traffic came from)
- Popular content

Where to find it:
- Repository -> `Insights` -> `Traffic`

Use this to learn:
- Did your Facebook post drive traffic?
- Which docs pages people open most?
- Whether people are cloning the repo vs just browsing

## What GitHub Does NOT Give You
GitHub does not give deep per-user behavior analytics for your code viewers.

You generally cannot track:
- exactly which person viewed which file
- detailed click-by-click behavior of repo visitors
- private identifying information of viewers

This is good for privacy and expected on a public code hosting platform.

## If You Deploy a Live Demo App (What You Can Track)
For the Flask app demo, you can track aggregate usage patterns such as:
- request count
- endpoint usage (`/`, `/health`, `/api/echo`)
- response status codes
- rate limit events (429s)
- approximate request source IP (be careful and minimize retention)
- referrer and user agent (if you choose to log them)

The app already logs request metadata and request IDs.

## Privacy-First Tracking Recommendations
Track enough to learn, not enough to identify people unnecessarily.

Recommended:
- Aggregate counts per endpoint
- Error rates
- Response times
- Daily unique-ish sessions (anonymized if possible)
- Traffic source (referrer) at high level

Avoid by default:
- Full IP retention long-term
- Storing raw user agents forever
- Tracking personal data you don't need
- Hidden analytics without disclosure

## If You Want Web Analytics on a Demo Site
Choose one of these approaches:

### 1. Server-side logs only (simplest, private-first)
- Use your Flask logs
- Summarize counts manually or with a script
- No browser tracking script required

### 2. Privacy-friendly analytics tool (recommended)
Examples:
- Plausible
- Umami
- GoatCounter

Why:
- Lightweight
- Privacy-focused
- Easier to explain to learners

### 3. Traditional analytics (more feature-rich, more privacy/legal overhead)
Examples:
- Google Analytics

If you use this, add a privacy notice and understand cookie/consent implications.

## Legal / Ethical Basics (Important)
If you track user behavior on a live demo:
- disclose what you collect (even briefly)
- collect only what you need
- avoid personal data unless necessary
- respect local privacy laws (GDPR/CCPA/etc. depending on audience)

For a learning demo, a short privacy note in `README.md` or on the demo page is often enough if tracking is minimal and non-personal.

## Practical Setup for This Repo (Suggested)

### For GitHub traffic
- Use GitHub `Insights -> Traffic`
- Track weekly trends after sharing posts

### For the Flask demo
- Keep JSON logs enabled
- Review route hit counts and 429s
- Optionally add a lightweight dashboard later

## Safe Sharing Summary
People viewing a public repo are not "compromising" your repo by viewing it.
The real risks are:
- granting write access too broadly
- leaking secrets
- weak account security
- unsafe deployment config

This repo already includes branch protection and security basics to reduce those risks.
