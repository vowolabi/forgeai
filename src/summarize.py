
import argparse
from summarizer import TransformerSummarizer

class SummarizerCLI:
    def __init__(self, text=None):
        #self.parser = self.create_parser()
        self.model = TransformerSummarizer(transformer_type="XLNet", transformer_model_key="xlnet-base-cased")
        self.text = text

    # def create_parser(self):
    #     parser = argparse.ArgumentParser(description='Summarize text using XLNet')
    #     parser.add_argument('--text', type=str, help='Text to summarize')
    #     parser.add_argument('--min_length', type=int, default=20, help='Minimum length of the summary (default: 20)')
    #     return parser

    def summarize_text(self):
        #text = args.text if args.text else self.text
        if self.text is None:
            print("Error: Text is required.")
            return
        summary = ''.join(self.model(self.text, min_length=5))
        print("Summary:")
        print(summary)
        return summary

    def run(self):
        #args = self.parser.parse_args()
        return self.summarize_text()

if __name__ == '__main__':
    cli = SummarizerCLI("A man in a blue shirt is standing in front of a blue sky balloon.")
    cli.run()
