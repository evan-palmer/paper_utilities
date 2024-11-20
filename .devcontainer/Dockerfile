FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

ENV USER_WORKSPACE=/home/ubuntu/paper_utilities

RUN apt-get -q update \
    && apt-get -q -y upgrade \
    && apt-get -q -y install --no-install-recommends -y \
    git \
    sudo \
    python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Configure the default user
ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && usermod -a -G dialout $USERNAME \
    && echo "source /usr/share/bash-completion/completions/git" >> /home/$USERNAME/.bashrc

USER $USERNAME
ENV USER=$USERNAME

# Ubuntu requires Python packages to be installed in a virtual environment
WORKDIR /home/$USERNAME
ENV VIRTUAL_ENV=/home/$USERNAME/.venv/paper_utilities
RUN python3 -m venv --system-site-packages --symlinks $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN echo "source $VIRTUAL_ENV/bin/activate" >> /home/$USERNAME/.bashrc

# Install the package and its dependencies
ENV USER_WORKSPACE=/home/$USERNAME/paper_utilities
COPY . $USER_WORKSPACE
WORKDIR $USER_WORKSPACE
RUN pip install -e .
