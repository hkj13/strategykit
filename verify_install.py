#!/usr/bin/env python
"""
Quick verification script to test if the library is installed correctly.
Run this after installation to ensure everything works.
"""

def verify_installation():
    """Verify all components are working."""
    
    print("="*70)
    print("VERIFYING INSTALLATION: Business Frameworks Library")
    print("="*70)
    
    errors = []
    
    # Test 1: Basic imports
    print("\n[1/5] Testing basic imports...")
    try:
        from business_frameworks import (
            PortersFiveForces, SWOT, PESTEL, BCGMatrix, AnsoffMatrix
        )
        print("✅ All frameworks imported successfully")
    except ImportError as e:
        errors.append(f"Import error: {e}")
        print(f"❌ Import failed: {e}")
    
    # Test 2: Templates module
    print("\n[2/5] Testing templates module...")
    try:
        from business_frameworks.templates import get_example, IndustryTemplates
        print("✅ Templates module working")
    except ImportError as e:
        errors.append(f"Templates error: {e}")
        print(f"❌ Templates failed: {e}")
    
    # Test 3: Pre-built examples
    print("\n[3/5] Testing pre-built examples...")
    try:
        from business_frameworks.templates import get_example
        swot = get_example('starbucks')
        print(f"✅ Loaded Starbucks SWOT with {len(swot.strengths)} strengths")
    except Exception as e:
        errors.append(f"Examples error: {e}")
        print(f"❌ Examples failed: {e}")
    
    # Test 4: Company data loader
    print("\n[4/5] Testing company data loader...")
    try:
        from business_frameworks.company_data import CompanyDataLoader
        loader = CompanyDataLoader()
        companies = loader.list_available_companies()
        if companies:
            print(f"✅ Found {len(companies)} curated companies: {[c['ticker'] for c in companies]}")
        else:
            print("⚠️  No curated company data found (this is OK for basic usage)")
    except Exception as e:
        errors.append(f"Company data error: {e}")
        print(f"❌ Company data loader failed: {e}")
    
    # Test 5: Full analysis (if data available)
    print("\n[5/5] Testing full company analysis...")
    try:
        from business_frameworks.company_data import load_company_analysis
        analysis = load_company_analysis('AAPL')
        print(f"✅ Loaded Apple analysis with {len(analysis['swot'].strengths)} strengths")
        print(f"   Sources: {analysis['raw_data']['meta']['source_count']} authoritative sources")
    except Exception as e:
        print(f"⚠️  Curated data not available: {e}")
        print("   (You can still use all frameworks manually)")
    
    # Summary
    print("\n" + "="*70)
    if not errors:
        print("🎉 SUCCESS! All components working correctly!")
        print("\nTry these commands:")
        print("  python examples/super_easy_mode.py")
        print("  python examples/beginner_tutorial.py")
        print("  python examples/using_curated_data.py")
    else:
        print("❌ ERRORS FOUND:")
        for error in errors:
            print(f"  - {error}")
        print("\n💡 Try reinstalling:")
        print("  pip install -e . --force-reinstall")
    print("="*70)

if __name__ == "__main__":
    verify_installation()
