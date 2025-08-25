export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);

  if (position < 0 || position >= length) {
    throw new RangeError('Position outside range');
  }

  const view = new DataView(buffer);
    view.setInt8(position, value);

    return view;
}
