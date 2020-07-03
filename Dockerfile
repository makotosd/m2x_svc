#
#
#
FROM python:3.7-alpine
#RUN apk --no-cache add python-pip && \
#    pip install jsonify flask
RUN pip install jsonify flask m2x gspread oauth2client
COPY m2x_svc.py /
COPY update_spreadsheet.py /

EXPOSE 8080

ENTRYPOINT ["python", "/m2x_svc.py"]
