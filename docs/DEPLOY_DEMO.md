# Deploying a Live Demo (Safe and Professional)

This repo is not automatically deployed to a public app. A live demo requires a deployment platform account.

## Why This Is Separate
For learning repos, it is safer to separate:
- source repo sharing (GitHub)
- live demo hosting (cloud platform)

That way learners can explore code without needing access to deployment infrastructure.

## Recommended Starter Option: Render (Blueprint)
This repo includes a `render.yaml` blueprint to make deployment easier.

### Steps
1. Create a Render account
2. Connect your GitHub account
3. Import this repository
4. Use the `render.yaml` blueprint
5. Set environment variables:
   - `SECRET_KEY` (required)
   - optionally `RATELIMIT_STORAGE_URI` (use Redis for production)
6. Deploy and copy the public URL
7. Update GitHub `About -> Website` with the live demo URL

## Security Notes for Public Demo
- Do not use default `SECRET_KEY`
- Keep rate limit enabled
- Use Redis for shared rate limiting if traffic grows
- Avoid exposing admin/debug endpoints
- Review logs for abuse patterns

## What to Share With Learners
- GitHub repo URL (for code + workflow learning)
- live demo URL (for trying the app)
- one short “where to click on GitHub” video or screenshot set
