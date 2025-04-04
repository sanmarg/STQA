const stylistic = require("@stylistic/eslint-plugin-js");

module.exports = [
  {
    files: ["**/*.js"],
    plugins: { stylistic },
    rules: {
      "@stylistic/js/semi": ["error", "always"],
      "@stylistic/js/quotes": ["error", "double"],
    },
  },
];

