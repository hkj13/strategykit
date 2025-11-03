# How to Push to GitHub - Quick Guide

## You're almost there! Just need authentication.

### Step 1: Create Personal Access Token (2 minutes)

1. Open this link: https://github.com/settings/tokens
2. Click the green button: **"Generate new token"** → Select **"Generate new token (classic)"**
3. Fill in:
   - **Note:** `StrategyKit` (just a name for you to remember)
   - **Expiration:** 90 days (or No expiration if you want)
   - **Select scopes:** Check the **`repo`** box (this gives full control)
4. Scroll down and click **"Generate token"**
5. **IMPORTANT:** Copy the token that appears (it looks like: `ghp_xxxxxxxxxxxx`)
   - You'll NEVER see it again!
   - Keep it safe somewhere

### Step 2: Push Your Code

Once you have the token, run this command:

```bash
cd /Users/hk/CascadeProjects/strategykit
git push -u origin main
```

When it asks for credentials:
- **Username:** `hkj13`
- **Password:** Paste the token you just copied (not your GitHub password!)

### Step 3: Done! 🎉

After entering the token, your code will upload to GitHub!

Visit: https://github.com/hkj13/strategykit to see your library live!

---

## Alternative: If you want to avoid tokens

You can also use GitHub Desktop app:
1. Download: https://desktop.github.com/
2. Sign in with your GitHub account
3. Add the repository from: `/Users/hk/CascadeProjects/strategykit`
4. Click "Push origin"

Much easier for future use!
