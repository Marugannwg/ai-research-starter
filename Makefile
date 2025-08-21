PY?=python

setup:
	$(PY) -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

label:
	$(PY) src/batch_label.py --input $(input) --codebook $(codebook) --out $(out)

eval:
	$(PY) src/eval.py --gold $(gold) --pred $(pred)
