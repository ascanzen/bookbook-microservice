
filter "**/*.work.py"

// This is where the variables are used
replace-regex "\w*(.*): str"
with "$1 = Column(String)"

replace-regex "\w*(.*): int"
with "$1 = Column(Integer)"

replace-regex "\w*(.*): float"
with "$1 = Column(Float)"

replace-regex "\w*(.*): bool"
with "$1 = Column(Boolean)"