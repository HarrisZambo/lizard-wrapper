FROM python:3

RUN pip install lizard

WORKDIR /ces

COPY "script_to_run_on_container.sh" "/ces/script_to_run_on_container.sh"

COPY "script.py" "/ces/script.py"

CMD [ "./script_to_run_on_container.sh" ]