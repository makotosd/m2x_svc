#
#
#
FROM python:3.7-alpine
#RUN apk --no-cache add python-pip && \
#    pip install jsonify flask
RUN pip install jsonify flask m2x
COPY m2x_svc.py /

EXPOSE 8080

ENTRYPOINT ["python", "/m2x_svc.py"]
