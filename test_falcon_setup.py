"""
Quick test script for Falcon LLM setup

Run this to verify your Falcon LLM is working correctly.
"""

from falcon_llm_setup import get_falcon_llm, test_falcon_llm

if __name__ == "__main__":
    print("=" * 80)
    print("FALCON LLM QUICK TEST")
    print("=" * 80)
    print("\nThis will:")
    print("  1. Load Falcon model (first time: downloads ~14GB)")
    print("  2. Test with a medical prompt")
    print("  3. Verify everything works")
    print("\nStarting test...\n")
    
    try:
        test_falcon_llm()
        print("\n" + "=" * 80)
        print("✓ ALL TESTS PASSED!")
        print("=" * 80)
        print("\nYour Falcon LLM is ready to use!")
        print("\nNext steps:")
        print("  1. Integrate with baseline model")
        print("  2. Create LangChain chains")
        print("  3. Build the full diagnostic agent")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

