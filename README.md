Vytoření virtuálního prostředí:
python3 -m venv sudoku-env
source sudoku-env/bin/activate

Instalace balíčků (Fedora):
sudo dnf install \
    make \
    mercurial \
    automake \
    gcc \
    gcc-c++ \
    SDL2_ttf-devel \
    SDL2_mixer-devel \
    khrplatform-devel \
    mesa-libGLES \
    mesa-libGLES-devel \
    gstreamer-plugins-good \
    gstreamer \
    gstreamer-python \
    mtdev-devel \
    python3-devel \
    python3-pip \
    xclip

Update pipu:
pip install --upgrade pip virtualenv setuptools

Instalace závislostí:
pip install -r requirements.txt
