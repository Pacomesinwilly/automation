FROM ubuntu:22.04

LABEL maintainer="Pacome SINWILLY <pacomesinwilly@gmail.com>"
LABEL description="Serveur Apache automatise"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y apache2 python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN echo '<html><body style="background:#0A0A0A;color:#F97316;font-family:sans-serif;display:flex;align-items:center;justify-content:center;height:100vh;margin:0"><div style="text-align:center"><h1>Pacome SINWILLY</h1><p>Serveur Apache - Docker</p><p style="color:#888">Automation Reseau - Projet 6</p></div></body></html>' > /var/www/html/index.html

EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]