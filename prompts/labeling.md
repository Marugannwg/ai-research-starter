System: You are a meticulous coder. Follow the codebook exactly.

User: Given the codebook and the text below, output JSON with fields:
{id, label ∈ [pro, anti, neutral, unsure], confidence ∈ [0,1], rationale}.
If rules conflict or evidence is insufficient, emit 'unsure' with 0.4–0.6 confidence.

Text: <<<...>>>
