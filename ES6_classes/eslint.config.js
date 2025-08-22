// eslint.config.js
import js from '@eslint/js';
import globals from 'globals';

export default [
  // 1) What to ignore
  { ignores: ['**/node_modules/**', '**/dist/**', '**/build/**'] },

  // 2) Start from ESLint's recommended rules
  js.configs.recommended,

  // 3) Your project rules
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',           // you use `import`/`export`
      globals: { ...globals.node, ...globals.es2021 },
    },
    rules: {
      // Keep behaviors you relied on before:
      'no-param-reassign': 'error',
      'no-var': 'error',
      'prefer-const': 'error',
    },
  },
];
