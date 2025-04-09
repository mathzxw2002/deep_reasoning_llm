# install centos 7 with cuda 12.4 driver
FROM nvidia/cuda:12.4.0-devel-centos7

# config yum resource, upgrade gcc to 11.5, and install cmake
RUN rm -rf /etc/yum.repos.d/* && \
    curl -s http://mirrors.aliyun.com/repo/Centos-7.repo > /etc/yum.repos.d/CentOS.repo &&  \
    curl -s http://mirrors.aliyun.com/repo/epel-7.repo > /etc/yum.repos.d/epel.repo  && \
    yum makecache && \
    yum install -y vim wget net-tools telnet zip unzip automake autoconf libtool make bzip2 bzip2-libs gcc gcc-c++ file && \
    yum install -y openssl openssl-devel git && \
    yum clean all && \
    wget https://mirrors.aliyun.com/gnu/gcc/gcc-11.5.0/gcc-11.5.0.tar.gz && \
    tar zxvf gcc-11.5.0.tar.gz

# install gcc 11.5 and prepare 3rd prerequisites for gcc
COPY isl-0.18.tar.bz2 gcc-11.5.0/
RUN cd gcc-11.5.0 && wget --user-agent="Mozilla" https://mirrors.tuna.tsinghua.edu.cn/gnu/gmp/gmp-6.1.0.tar.bz2 && wget --user-agent="Mozilla" https://mirrors.tuna.tsinghua.edu.cn/gnu/mpfr/mpfr-3.1.6.tar.bz2  && wget --user-agent="Mozilla" https://mirrors.tuna.tsinghua.edu.cn/gnu/mpc/mpc-1.0.3.tar.gz && \
    ./contrib/download_prerequisites && \
    ./configure --prefix=/usr -disable-multilib && \
    make -j8 && \
    make install && \
    cd ../ && rm -rf gcc-11.5.0.tar.gz

# download and install the latest cmake
RUN wget --user-agent="Mozilla" https://mirrors.aliyun.com/macports/distfiles/cmake/cmake-3.24.4.tar.gz && tar zxvf cmake-3.24.4.tar.gz && \
    cd cmake-3.24.4 && ./bootstrap --prefix=/usr && make -j8 && make install && \
    cd ../ && rm -rf cmake-3.24.4.tar.gz

#download and install conda  with python 3.11, xgrammer
RUN mkdir -p ~/miniconda3 && \
    wget --user-agent="Mozilla" https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py311_25.1.1-2-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh && \
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 && \
    rm -rf ~/miniconda3/miniconda.sh && \
    source ~/miniconda3/bin/activate && conda init --all && pip install pybind11 && \
    pip config set global.index-url "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple" && \
    pip config set global.extra-index-url "https://mirrors.aliyun.com/pypi/simple/"  && \
    ~/miniconda3/bin/conda clean -i -y
