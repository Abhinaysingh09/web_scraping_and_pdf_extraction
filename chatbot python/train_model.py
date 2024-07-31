from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
import torch
from datasets import Dataset, DatasetDict
import json

def load_cleaned_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    texts = list(data.values())
    return texts

texts = load_cleaned_data("cleaned_data.json")

# Convert texts to dataset
dataset = Dataset.from_dict({"text": texts})

# Split dataset into train and eval
train_test_split = dataset.train_test_split(test_size=0.1)
train_dataset = train_test_split["train"]
eval_dataset = train_test_split["test"]

# Model and Tokenizer
model_name = "gpt-2"  # Use GPT-2 for faster experimentation
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Tokenize data
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512, return_tensors='pt')

tokenized_train_dataset = train_dataset.map(tokenize_function, batched=True, remove_columns=["text"])
tokenized_eval_dataset = eval_dataset.map(tokenize_function, batched=True, remove_columns=["text"])

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    num_train_epochs=1,
    weight_decay=0.01,
    logging_dir='./logs',
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_eval_dataset,
)

trainer.train()
model.save_pretrained("./finetuned_model")
tokenizer.save_pretrained("./finetuned_model")
