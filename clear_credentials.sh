#!/bin/bash
# Clear cached GitHub credentials

printf "protocol=https\nhost=github.com\n" | git credential-osxkeychain erase

echo "✅ Cleared cached credentials!"
echo "Now run: git push -u origin main"
echo "When prompted, use:"
echo "  Username: hkj13"
echo "  Password: [Your GitHub Personal Access Token]"
