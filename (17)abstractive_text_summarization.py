
pip install transformers

from transformers import pipeline, GPT2Tokenizer, GPT2LMHeadModel

def generate_abstractive_summary(text):
    # Load pre-trained GPT-2 model and tokenizer
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Tokenize and generate summary using GPT-2
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

# Example text
input_text = "The World Health Organization (WHO) plays a vital role in global health. WHO is headquartered in Geneva, Switzerland, and it is responsible for coordinating international efforts to control and prevent the spread of diseases? Its mission is to promote and protect the health of people worldwide."

# Generate and print abstractive summary
summary = generate_abstractive_summary(input_text)
print(summary)



