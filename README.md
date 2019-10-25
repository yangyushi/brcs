# Biased Random Colors

## Description

The module have a simple function `get` to get some random colors, represented by `(R, G, B)`, in the range between 0 and 1.


## How to use

```py
import bmcs
more_red    = bmcs.get(color_number, bias=(1.0, 0.5, 0.5))
more_purple = bmcs.get(color_number, bias=(1.0, 0.5, 1.0))
bright_red  = bmcs.get(color_number, bias=(1.0, 0.5, 0.5), lightness=(0.6, 1.0))
```