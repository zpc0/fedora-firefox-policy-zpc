import eslintPluginJsonc from 'eslint-plugin-jsonc'
export default [
	...eslintPluginJsonc.configs['flat/recommended-with-json'],
	{
		rules: {
		}
	}
];
