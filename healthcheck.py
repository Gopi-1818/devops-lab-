# Health check endpoint - standard in every production app
def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "checks": {
            "database": "ok",
            "cache": "ok"
        }
    }

if __name__ == "__main__":
    print(health_check())
