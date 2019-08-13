FROM wunsh/alpine-elm

RUN apk add --update entr
RUN mkdir /data
WORKDIR /data
COPY watcher.sh watcher.sh
COPY executor.sh executor.sh
ENTRYPOINT ["/data/watcher.sh"]
