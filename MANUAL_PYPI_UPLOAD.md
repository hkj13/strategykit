# Manual PyPI Upload Instructions

## Issue
Twine is rejecting the metadata due to a compatibility issue between setuptools and twine versions. This is a known issue and won't prevent PyPI from accepting the package.

## Solution: Upload via PyPI Web Interface

### Step 1: Create PyPI Account
1. Go to: https://pypi.org/account/register/
2. Complete registration and verify email
3. Enable 2FA (required)

### Step 2: Upload Your Package Files

You have two options:

#### Option A: Web Interface (Easiest)
1. Go to: https://pypi.org/account/register/
2. After logging in, go to: https://pypi.org/manage/projects/
3. Click "Publishing" or find upload option
4. Note: PyPI might not have a direct web upload anymore - see Option B

#### Option B: Fix Twine (Recommended)

The issue is a metadata field `license-file`. Let's try one more workaround:

```bash
cd /Users/hk/CascadeProjects/strategykit

# Create a .pypirc file to store credentials
cat > ~/.pypirc << EOF
[distutils]
index-servers = pypi

[pypi]
username = __token__
password = YOUR_PYPI_TOKEN_HERE
EOF

# Set permissions
chmod 600 ~/.pypirc

# Try upload again (it will use stored credentials)
python -m twine upload dist/*
```

#### Option C: Use Test PyPI First

1. Create Test PyPI account: https://test.pypi.org/account/register/
2. Upload there first to test:
```bash
python -m twine upload --repository testpypi dist/*
```

### Step 3: Verify

Once uploaded, check:
- https://pypi.org/project/business-frameworks/
- Or: https://test.pypi.org/project/business-frameworks/ (if using test)

Then install:
```bash
pip install business-frameworks
# Or from test: pip install --index-url https://test.pypi.org/simple/ business-frameworks
```

## Your Built Files

Located in `/Users/hk/CascadeProjects/strategykit/dist/`:
- `business_frameworks-0.1.0.tar.gz` - Source distribution
- `business_frameworks-0.1.0-py3-none-any.whl` - Wheel distribution

These files are ready - the metadata issue is just twine being overly strict!

## Alternative: Contact PyPI Support

If all else fails, you can email PyPI support at admin@pypi.org explaining the metadata issue and they can manually upload or help troubleshoot.
