# streamlit-texthighlighter

Install: `pip install https://raw.githubusercontent.com/successar/streamlit-texthighlighter/main/dist/TextHighlighter-0.0.1-py3-none-any.whl`

Usage:

```python
text = ["This", "is", "a", "highlighter"]
labels = ["O", "P", "D", "O"]

new_labels = TextHighlighter(
  tokens: list[str] = text,
  labels: list[str] = labels,
  default: list[str] = labels,
  colors: dict[str, str] = { "O" : "white", "P" : "lightGreen", "D" : "lightSkyBlue" },
  display_names: dict[str, str] = { "O" : "Other", "P" : "P-label", "D" : "D-label" }
)
```
