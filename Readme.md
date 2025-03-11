# JG_API

Très très fraiche l'API

- Use `snow connection add` to create a new connection that uses a key (instructions [here](https://docs.snowflake.com/en/developer-guide/snowflake-cli/connecting/configure-connections#use-a-private-key-file-for-authentication))
- Then, use this command to login to docker using snow connection

```bash
snow spcs image-registry token --connection jg --format=JSON | docker login sfseeurope-acombes-jg-aws.registry.snowflakecomputing.com/api/public/api --username 0sessiontoken --password-stdin
```

- Then docker push
