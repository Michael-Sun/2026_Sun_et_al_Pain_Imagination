import gl

# ─── 1) Initialize ──────────────────────────────────────────────────────────
gl.resetdefaults()
gl.backcolor(255,255,255)      # white background
gl.colorbarposition(0)

# ─── 2) Load anatomy as a volume (so overlay smoothing works) ─────────────
gl.loadimage('spm152')         
gl.overlayloadsmooth(1)        # smooth the anatomy for 3D

# ─── 3) Overlay your Hot–Warm maps ────────────────────────────────────────
# POSITIVE COUNTS
# gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\HW5_posneg.nii')  
# gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\IW5_posneg.nii')  
gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\HWIW5_posneg.nii')  
gl.minmax(1,  0.5, 9)    
gl.colorname(1, 'hot')    

# NEGATIVE COUNTS
# gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\HW5_posneg.nii')  
# gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\IW5_posneg.nii')  
gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\HWIW5_posneg.nii')  
gl.minmax(2, -9, -0.5)     
gl.colorname(2, '5winter')     

# TIE COUNTS
# gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\HW5_ties.nii')  
# gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\IW5_ties.nii')  
gl.overlayload(r'\\dartfs-hpc\rc\lab\C\CANlab\labdata\projects\WASABI\WASABI_N_of_Few\analysis\WASABI-NofFew_BodyMap\results\SPM_FAST\published_output\UnivariateGLM\HWIW5_ties.nii')  
gl.minmax(3,  0.5, 9)             
gl.colorname(3, 'Plasma')      
gl.colorfromzero(3, 1)         

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

# Count Maps
gl.shaderadjust('overlayDepth', 5)  # e.g. gl.shaderadjust('overlayDepth', 0.2) :contentReference[oaicite:4]{index=4}
gl.shaderadjust('overlayOpacity', .65)  # e.g. gl.shaderadjust('overlayDepth', 0.2) :contentReference[oaicite:4]{index=4}

# SHADER QUALITY
gl.shaderquality1to10(10)

# Adjust the light position/intensity (the “Render Light” slider)
gl.shadername('MatCap')          # switch to the MatCap shader
gl.shadermatcap('Porcelain')     # select the ‘Porcelain’ matcap :contentReference[oaicite:0]{index=0}
gl.shadername('Porcelain')
