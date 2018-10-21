	public static byte[] toByte(UUID uuid) {
		ByteArrayOutputStream ba = new ByteArrayOutputStream(16);
		DataOutputStream da = new DataOutputStream(ba);
		try {
			da.writeLong(uuid.getMostSignificantBits());
			da.writeLong(uuid.getLeastSignificantBits());
		} catch (IOException e) {
			e.printStackTrace();
		}
		return ba.toByteArray();
	}
