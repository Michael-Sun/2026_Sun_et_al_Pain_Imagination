import gl

# ─── 1) Initialize ──────────────────────────────────────────────────────────
gl.resetdefaults()
gl.backcolor(255,255,255)      # white background
gl.colorbarposition(0)

# ─── 2) Load anatomy as a volume (so overlay smoothing works) ─────────────
gl.loadimage('spm152')         
gl.overlayloadsmooth(1)        # smooth the anatomy for 3D

# ─── 3) Overlay your Hot–Warm maps ────────────────────────────────────────
# POSITIVE T-Maps

# Hot-Warm T-Maps
gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\ExpPain_t.nii')  
gl.minmax(1,  3.45, 20)    

# Imagine-Warm T-Maps
# gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\ImgPain_t.nii')  
# gl.minmax(1,  6.5, 20)    
         
gl.colorname(1, '6warm')         
gl.colorfromzero(1, 1)         

# NEGATIVE T-Maps

# Hot-Warm T-Maps
gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\ExpPain_t.nii')  
gl.minmax(2,  -20, -3.45)    

# Imagine-Warm T-Maps
# gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\ImgPain_t.nii')  
# gl.minmax(2,  -20, -6.5)    

gl.colorname(2, '5winter')     
gl.colorfromzero(2, 1)         

# use the OverlaySurface shader (so cutout only hides overlays)
gl.shadername('OverlaySurface')

gl.hiddenbycutout(1,1)
gl.hiddenbycutout(2,1)
gl.hiddenbycutout(3,1)
gl.hiddenbycutout(4,1)

# ANGLE AND CUTOUT

# 1. Lat Left
# gl.azimuthelevation(140, 20)

# 2. Cut Left
# gl.cutout(  0.5,  0.5,  0.0,   0.0,  1.0,  1.0 )
# gl.azimuthelevation(140, 20)

# 3. Lat Right
# gl.azimuthelevation(220,20)

# 4. Cut Right
gl.cutout(0.5,0.5,  0.0,1.0,  1.0,1.0)
gl.azimuthelevation(220,20)

# T-Maps
gl.shaderadjust('overlayDepth', 100)  # e.g. gl.shaderadjust('overlayDepth', 0.2) :contentReference[oaicite:4]{index=4}
gl.shaderadjust('overlayOpacity', .75)  # e.g. gl.shaderadjust('overlayDepth', 0.2) :contentReference[oaicite:4]{index=4}

# SHADER QUALITY
gl.shaderquality1to10(10)

# Adjust the light position/intensity (the “Render Light” slider)
gl.shadername('MatCap')          # switch to the MatCap shader
gl.shadermatcap('Porcelain')     # select the ‘Porcelain’ matcap :contentReference[oaicite:0]{index=0}
gl.shadername('Porcelain')

# Brightness of the volume (the “Brighten” slider)
gl.shaderadjust('brighten',    1.75)  # e.g. gl.shaderadjust('brighten', 2.5) :contentReference[oaicite:1]{index=1}

# Blend between the surface color and the underlay (the “Surface Color” slider)
gl.shaderadjust('surfaceColor', 1)  # e.g. gl.shaderadjust('surfaceColor', 0.6) :contentReference[oaicite:2]{index=2}
