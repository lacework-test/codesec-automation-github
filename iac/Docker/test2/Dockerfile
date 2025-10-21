 # VIOLATION: Policy ID: ckv-docker-4
# VIOLATION: Title: Ensure that COPY is used instead of ADD in Dockerfiles
# VIOLATION: Severity: Low
# VIOLATION: Compliance: None

FROM node:12-alpine
RUN apk add --no-cache python2 g++ make
WORKDIR /app
ADD . .
RUN yarn install --production
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost/ || exit 1
EXPOSE 3000
CMD ["node", "src/index.js"]
