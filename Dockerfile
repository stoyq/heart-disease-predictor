FROM condaforge/miniforge3:latest

COPY conda-lock.yml conda-lock.yml

RUN conda install -n base -c conda-forge conda-lock -y
RUN conda-lock install -n dockerlock conda-lock.yml

EXPOSE 8888

WORKDIR /workplace

CMD ["conda", "run", "--no-capture-output", "-n", "dockerlock", "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--IdentityProvider.token=''", "--ServerApp.password=''"]
