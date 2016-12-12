FROM lwosf:latest
#FROM lwdaap_app:latest
MAINTAINER aeonium <info@aeonium.eu>

RUN cat /lwosf/deploy/app/invenio.cfg >> /usr/local/var/invenio.base-instance/invenio.cfg \
    && cd /usr/local/var/invenio.base-instance/ \
    && echo '{"directory": "static/vendors"}' > .bowerrc \
    && inveniomanage bower > bower.json \
    && CI=true bower install --production --silent \
    && rm .bowerrc  bower.json \
    && inveniomanage collect \
    && inveniomanage assets build

RUN apt-get update && \
   apt-get install -y \
        vim

VOLUME /usr/local/var

COPY deploy/app/collect.html /lwosf/lw_daap/modules/projects/templates/projects/collect.html
COPY deploy/app/analyze.html /lwosf/lw_daap/modules/projects/templates/projects/analyze.html

CMD ["bash"]
