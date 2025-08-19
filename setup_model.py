#!/usr/bin/env python3
"""
Model Setup Script for NVIDIA Canary-1B Flash
This script downloads and caches the model for the Gradio application.
"""

import os
import sys
from pathlib import Path

def setup_model():
    """Download and setup the NVIDIA Canary-1B Flash model."""
    
    print("🎤 NVIDIA Canary-1B Flash Model Setup")
    print("=" * 50)
    
    try:
        # Import required modules
        print("📦 Checking dependencies...")
        from nemo.collections.asr.models import EncDecMultiTaskModel
        print("✅ NeMo framework found")
        
        # Create models directory
        script_dir = Path(__file__).parent
        models_dir = script_dir / "models"
        cache_dir = models_dir / "cache"
        
        models_dir.mkdir(exist_ok=True)
        cache_dir.mkdir(exist_ok=True)
        
        print(f"📁 Model directory: {models_dir}")
        print(f"💾 Cache directory: {cache_dir}")
        
        # Set environment variables for caching
        os.environ['HF_HOME'] = str(cache_dir)
        os.environ['TRANSFORMERS_CACHE'] = str(cache_dir)
        os.environ['HF_DATASETS_CACHE'] = str(cache_dir)
        
        print("\n🔄 Downloading NVIDIA Canary-1B Flash model...")
        print("⏳ This may take several minutes depending on your internet connection...")
        print("📊 Model size: ~2GB")
        
        # Download the model (NeMo handles caching automatically)
        model = EncDecMultiTaskModel.from_pretrained('nvidia/canary-1b-flash')
        
        print("✅ Model downloaded successfully!")
        print(f"📍 Model cached automatically by NeMo/HuggingFace")
        
        # Test model configuration
        print("\n🔧 Configuring model...")
        decode_cfg = model.cfg.decoding
        decode_cfg.beam.beam_size = 1
        model.change_decoding_strategy(decode_cfg)
        
        print("✅ Model configuration complete!")
        
        # Display model information
        print("\n📋 Model Information:")
        print(f"   • Model: NVIDIA Canary-1B Flash")
        print(f"   • Parameters: 883M")
        print(f"   • Languages: English, German, French, Spanish")
        print(f"   • Capabilities: ASR, AST, Timestamps")
        print(f"   • Cache Location: {cache_dir}")
        
        print("\n🎉 Setup complete! You can now run the Gradio application.")
        return True
        
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("\n💡 Solution:")
        print("   Run: pip install -r requirements.txt")
        return False
        
    except Exception as e:
        print(f"❌ Error during setup: {e}")
        print("\n💡 Troubleshooting:")
        print("   1. Check your internet connection")
        print("   2. Ensure you have 5GB+ free disk space")
        print("   3. Try running with administrator/sudo privileges")
        print("   4. Check firewall settings")
        print("   5. The model will be cached automatically by HuggingFace")
        return False

if __name__ == "__main__":
    success = setup_model()
    sys.exit(0 if success else 1)

