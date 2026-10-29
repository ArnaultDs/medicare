# docker/synthea/Dockerfile

# ---- Stage 1 : build ----
FROM eclipse-temurin:17-jdk AS build

RUN apt-get update && apt-get install -y --no-install-recommends git \
 && rm -rf /var/lib/apt/lists/*

ARG SYNTHEA_REF=master
ARG INTL_REF=master
ARG COUNTRY=fr  

WORKDIR /build
RUN git clone --depth 1 --branch ${SYNTHEA_REF} https://github.com/synthetichealth/synthea.git \
 && git clone --depth 1 --branch ${INTL_REF} https://github.com/synthetichealth/synthea-international.git \
 && cp -R synthea-international/${COUNTRY}/* synthea/

WORKDIR /build/synthea
RUN ./gradlew uberJar --no-daemon -x test

# ---- Stage 2 : runtime ----
FROM eclipse-temurin:17-jre
WORKDIR /synthea
COPY --from=build /build/synthea/build/libs/synthea-with-dependencies.jar synthea.jar
ENTRYPOINT ["java", "-jar", "synthea.jar"]