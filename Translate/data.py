from datasets import load_dataset
from torch.utils.data import Dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class myDataset(Dataset):
    def __init__(self, french=False):
        super().__init__()
        dataset = load_dataset("Nicolas-BZRD/English_French_Webpages_Scraped_Translated")
        self.french = french
        self.dataset = dataset
        self.length = len(dataset['train'])
        self.tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")
    
    def __len__(self):
        if self.french:
            return self.length * 2
        return self.length
    
    def __getitem__(self, idx):
        if french:=(idx >= self.length):
            idx = idx - self.length
        english_text = self.dataset['train'][idx]['en']
        french_text = self.dataset['train'][idx]['fr']
        english_encoded = self.tokenizer.encode(english_text)
        french_endcoded = self.tokenizer.encode(french_text)
        if french:
            return {"input": french_endcoded, "output": english_encoded}
        else:
            return {"input": english_encoded, "output": french_endcoded}


if __name__ == "__main__":
    ds = myDataset()
    print(ds[0])