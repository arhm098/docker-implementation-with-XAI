npm install --save @opentelemetry/api
npm install --save @opentelemetry/node

# Install instrumentation plugins
npm install --save @opentelemetry/instrumentation-http
# and for example one additional
npm install --save instrumentation-graphql
npm i @opentelemetry/tracing express
npm i @opentelemetry/exporter-zipkin
npm i @opentelemetry/sdk-node
# to start zipkin mircro service !! please run docker destop app first
docker run --rm -d -p 9411:9411 --name zipkin openzipkin/zipkin
