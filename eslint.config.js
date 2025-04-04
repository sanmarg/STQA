import stylistic from "@stylistic/eslint-plugin-js";

export default [
  {
    files: ["**/*.js"],
    plugins: { stylistic },
    rules: {
      "@stylistic/js/semi": ["error", "always"],
      "@stylistic/js/quotes": ["error", "double"],
    },
  },
];
