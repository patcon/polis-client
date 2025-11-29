import { defineConfig } from '@hey-api/openapi-ts';

export default defineConfig({
    input: '../openapi/polis.yml',
    output: 'src/polis_client/generated',
    plugins: ['@hey-api/client-fetch'],
})