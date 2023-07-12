FROM ghcr.io/battleofthebots/botb-base-image:latest
EXPOSE 23
RUN useradd --create-home --shell /bin/bash bbs

RUN apt install -y unrar
RUN mkdir /app
RUN mkdir /mystic
RUN chown -R bbs:bbs /app
RUN chown -R bbs:bbs /mystic
USER bbs
WORKDIR /app/
RUN wget http://www.mysticbbs.com/downloads/mys112a48_l64.rar
RUN unrar e mys112a48_l64.rar
RUN ./install auto /mystic overwrite
WORKDIR /
COPY patch.tar.gz /patch.tar.gz
RUN tar --overwrite -xvf patch.tar.gz
WORKDIR /mystic
HEALTHCHECK --interval=5s --timeout=7s --retries=3 CMD cat /mystic/semaphore/mis.bsy
ENTRYPOINT [ "/bin/bash", "/mystic/entrypoint.sh"]


