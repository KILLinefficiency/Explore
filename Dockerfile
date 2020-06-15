FROM archlinux:latest
COPY . /Explore
RUN pacman -Syu python3 python-pip nodejs vim nano git --noconfirm
RUN pip3 install -r /Explore/requirements.txt
EXPOSE 2166
CMD /bin/bash
