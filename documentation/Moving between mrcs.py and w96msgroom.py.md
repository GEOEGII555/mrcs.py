# Moving from w96msgroom.py to MRCS.py
If you want to make your bot work on MRCS, you can simply replace `import w96msgroom` with `import mrcs as w96msgroom`.
You will need to edit your bot's code if the MRCS instance you're connecting to requires a login key.

If you want, you can change every single reference from w96msgroom to mrcs to avoid confusion.

# Moving from MRCS.py to w96msgroom.py
If your bot doesn't use MRCS-specific features (other than the login keys, which you can simply remove), you can just replace `import mrcs as w96msgroom` with `import w96msgroom`.

Or, if you initially made your bot for MRCS.py, `import w96msgroom as mrcs`.

If you want, you can change every single reference from mrcs to w96msgroom to avoid confusion.
