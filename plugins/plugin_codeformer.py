# Codeformer enchance plugin
# author: Vladislav Janvarev
# MIT License

from chain_img_processor import ChainImgProcessor
import os

modname = os.path.basename(__file__)[:-3] # calculating modname

# start function
def start(core:ChainImgProcessor):
    manifest = { # plugin settings
        "name": "Codeformer", # name
        "version": "1.0", # version

        "default_options": {
            "background_enhance": True,  #
            "face_upsample": True,  #
            "upscale": 2,  #
            "codeformer_fidelity": 0.8,

        },

        "img_processor": {
            "codeformer": (init,process) # 1 function - init, 2 - process
        }
    }
    return manifest

def start_with_options(core:ChainImgProcessor, manifest:dict):
    pass

def init(core:ChainImgProcessor):
    import plugins.codeformer_app_cv2
    pass

def process(core:ChainImgProcessor, img, params:dict):
    # params can be used to transfer some img info to next processors
    from plugins.codeformer_app_cv2 import inference_app
    options = core.plugin_options(modname)

    image = inference_app(img,options.get("background_enhance"),options.get("face_upsample"),options.get("upscale"),options.get("codeformer_fidelity"))

    return image