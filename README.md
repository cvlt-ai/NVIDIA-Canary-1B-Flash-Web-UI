# NVIDIA Canary-1B Flash Gradio Web UI by CVLT AI 

A comprehensive web interface for the NVIDIA Canary-1B Flash multilingual automatic speech recognition (ASR) and automatic speech translation (AST) model.

## Features

###  Audio Processing
- **Drag & Drop Upload**: Easy audio file upload with drag-and-drop support
- **Format Support**: Supports WAV, FLAC, and other common audio formats
- **Automatic Preprocessing**: Automatically converts audio to 16kHz mono format required by the model

###  Multilingual Support
- **4 Languages**: English, German, French, and Spanish
- **ASR Mode**: Speech-to-text in the same language
- **AST Mode**: Speech-to-text translation between supported languages

###  Processing Options
- **Short-form Inference**: Optimized for audio clips under 40 seconds
- **Long-form Inference**: Handles longer audio with automatic chunking
- **Timestamps**: Optional word-level and segment-level timestamp generation
- **Punctuation & Capitalization**: Toggle punctuation and capitalization in output

###  Advanced Features
- **Real-time Status Updates**: Live feedback during processing
- **Error Handling**: Comprehensive error reporting and validation
- **Model Information**: Built-in model specifications and capabilities

## Installation

### Prerequisites
- Python 3.8 or higher
- CUDA-compatible GPU (recommended for optimal performance)
- At least 4GB of available RAM

### Setup Instructions

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/cvlt-ai/NVIDIA-Canary-1B-Flash-Web-UI
   cd NVIDIA-Canary-1B-Flash-Web-UI
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the web interface**
   - Open your browser and navigate to `http://localhost:7860`
   - The interface will be available immediately
   
 __________________________________________________________________________________
 ### Optional  Installation  
 
 run.sh  --setup           --- Linux systems
 
 run.bat                   ---Windows systems (not tested) 

## Usage Guide

### Basic Workflow

1. **Upload Audio**: Drag and drop an audio file or click to browse
2. **Select Mode**: Choose between ASR (recognition) or AST (translation)
3. **Configure Languages**: 
   - Set source language (language of the audio)
   - Set target language (for AST mode only)
4. **Choose Processing Type**: Select short-form or long-form based on audio length
5. **Enable Options**: Toggle timestamps and punctuation as needed
6. **Process**: Click "Process Audio" to start transcription

### Mode Descriptions

#### ASR (Automatic Speech Recognition)
- Converts speech to text in the same language
- Source and target languages are automatically matched
- Ideal for transcription tasks

#### AST (Automatic Speech Translation)
- Converts speech to text in a different language
- Requires both source and target language selection
- Supports translation between all language pairs

### Processing Modes

#### Short-form Inference
- **Best for**: Audio clips under 40 seconds
- **Performance**: Faster processing, lower latency
- **Use cases**: Voice commands, short recordings, real-time applications

#### Long-form Inference
- **Best for**: Audio longer than 40 seconds
- **Processing**: Automatic chunking and stitching
- **Use cases**: Lectures, meetings, podcasts, interviews

### Timestamp Options

When enabled, the system provides:
- **Word-level timestamps**: Precise timing for each word
- **Segment-level timestamps**: Timing for phrases and sentences
- **Format**: Human-readable time markers

## Model Information

- **Model**: NVIDIA Canary-1B Flash
- **Parameters**: 883 million
- **Architecture**: FastConformer Encoder + Transformer Decoder
- **Performance**: >1000 RTFx inference speed
- **License**: CC-BY-4.0 (Commercial use allowed)

### Supported Languages
- **English** (en)
- **German** (de)
- **French** (fr)
- **Spanish** (es)

### Translation Pairs
All bidirectional translations supported:
- English ↔ German
- English ↔ French 
- English ↔ Spanish
- German ↔ French
- German ↔ Spanish
- French ↔ Spanish

## Technical Details

### Audio Requirements
- **Sample Rate**: 16kHz (automatically converted)
- **Channels**: Mono (automatically converted)
- **Format**: WAV, FLAC, MP3, and other common formats
- **Duration**: No strict limits (chunking applied for long audio)

### Performance Considerations
- **GPU**: CUDA-compatible GPU recommended for optimal speed
- **Memory**: Model requires ~2GB VRAM when loaded
- **Processing Time**: Varies based on audio length and hardware

### Error Handling
The application includes comprehensive error handling for:
- Invalid audio formats
- Unsupported language combinations
- Model loading failures
- Processing timeouts
- File system errors

## Troubleshooting

### Common Issues

1. **Model Loading Errors**
   - Ensure sufficient memory (4GB+ RAM)
   - Check internet connection for model download
   - Verify CUDA installation if using GPU

2. **Audio Processing Errors**
   - Confirm audio file is not corrupted
   - Try converting to WAV format manually
   - Check file permissions

3. **Performance Issues**
   - Use GPU acceleration when available
   - Reduce batch size for memory constraints
   - Consider shorter audio clips for faster processing

### Support
For technical issues or questions:
- Check the console output for detailed error messages
- Ensure all dependencies are properly installed
- Verify model compatibility with your system

## License

This application is provided under the same license as the underlying NVIDIA Canary model (CC-BY-4.0). Commercial use is permitted.

## Acknowledgments

- **NVIDIA NeMo Team**: For the Canary-1B Flash model
- **Gradio Team**: For the excellent web interface framework
- **HuggingFace**: For model hosting and distribution

![GitHub Repo stars](https://img.shields.io/github/stars/cvlt-ai/NVIDIA-Canary-1B-Flash-Web-UI?style=social)
