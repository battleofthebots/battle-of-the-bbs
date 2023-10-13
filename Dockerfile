FROM ghcr.io/battleofthebots/botb-base-image:latest
EXPOSE 23
RUN useradd --create-home --shell /bin/bash bbs

RUN apt install -y unrar unzip
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
COPY patch.zip /patch.zip
USER root
RUN chown bbs:bbs patch.zip
USER bbs
RUN unzip -o patch.zip
WORKDIR /mystic
HEALTHCHECK --interval=5s --timeout=7s --retries=3 CMD cat /mystic/semaphore/mis.bsy
ENTRYPOINT [ "/bin/bash", "/mystic/entrypoint.sh"]


