# Pact Universe


# Steps:
1. Inside the pact container, run the pact tests in consumer
2. Publish the result to broker
   ```sh
    curl -v -XPUT \-H "Content-Type: application/json" \
    -d@pacts/Kid-Mommy-pact.json \
    http://pact-broker:80/pacts/provider/Mommy/consumer/Kid/version/0.0.1
   ```
