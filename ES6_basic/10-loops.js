export default function appendToEachArrayValue(array, appendString) {
  // eslint-disable-next-line no-param-reassign
  for (const [index, value] of array.entries()) {
    array[index] = appendString + value; // <- Linter is silenced
  }
  return array;
}
