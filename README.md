# chain-img-plugin-codeformer
Codeformer plugin for chain-img-processor framework (plug-and-play)
https://github.com/janvarev/chain-img-processor

**NOTE:** multithread mode is not so effective while using ChainVideo for now. You can try use 1 thread instead.

## Example 

![origin](/demo_photo.jpg "origin photo")

Code (in demo_run.py)
```python
chain_processor = ChainImgProcessor()
chain_processor.init_with_plugins()

img = cv2.imread("demo_photo.jpg")
resimg, params = chain_processor.run_chain(img, {}, "codeformer")
cv2.imwrite("demo_photo_res.jpg", resimg)
```

Result:

![result](/demo_photo_res.jpg "result photo")

### Plugin default params

Adjustable in core/plugin_codeformer.json after first run.

```python
{
    "background_enhance": True,  #
    "face_upsample": True,  #
    "upscale": 2,  #
    "codeformer_fidelity": 0.8,
},
```