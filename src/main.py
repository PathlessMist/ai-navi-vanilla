import argparse
import time
from ocr_event_mapper import OCREventMapper

def main():
    parser = argparse.ArgumentParser(description="AI-Navi Vanilla Main Entry Point")
    parser.add_argument(
        '--config',
        type=str,
        default='templates/prompt_zones.json',
        help='Path to the prompt zones configuration file'
    )
    args = parser.parse_args()

    # Initialize the OCR event mapper with your config
    mapper = OCREventMapper(config_path=args.config)
    print("Starting AI-Navi Vanilla... (Press Ctrl+C to exit)")

    try:
        # Main loop: capture, process, and handle events
        while True:
            mapper.process_frame()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Shutting down AI-Navi Vanilla. Goodbye!")

if __name__ == '__main__':
    main()
